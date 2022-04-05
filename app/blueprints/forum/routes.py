from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
from app.models import db, User, Post
from flask_login import login_user, current_user, logout_user, login_required
from .forum_forms import PostForm

forum = Blueprint('forum', __name__, template_folder='forum_templates', url_prefix='/forum')

#  Shows all the posts from every user ever posted and they can post something 
@forum.route('/feed', methods=['GET', 'POST'])
def feed():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=9)

    form = PostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            newpost = Post()
            newpost.title = form.title.data
            newpost.body = form.new_post.data
            newpost.user_id = current_user.id
            db.session.add(newpost)
            db.session.commit()
            flash('New post created :)', 'success')
            return redirect(url_for('forum.feed'))   
    return render_template('feed.html', posts=posts, form=form)

# set a route to users to see thier comments 
@forum.route('/<string:username>')
def userProfile(username):
    user = User.query.filter_by(username=username).first()
    if user:
        posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).all()
    
    return render_template('userprofile.html', user=user, posts=posts)


# user can delete their posts only
@forum.route('/delete/<int:pid>')
@login_required
def deletePost(pid):
    to_delete = Post.query.get(pid)
    if current_user.id == to_delete.user_id:
        db.session.delete(to_delete)
        db.session.commit()
        flash('Post deleted successfully.', 'info')
        return redirect(url_for('forum.userProfile', username=current_user.username))
    return jsonify({'Come on': 'you shouldnt be here'}), 403
