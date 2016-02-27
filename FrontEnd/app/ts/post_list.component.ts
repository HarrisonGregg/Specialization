import {Component} from 'angular2/core';
import {Post} from './post';

@Component({
	selector: 'post-list',
	templateUrl: '/app/templates/post_list.component.html',
	styleUrls: ['/css/app.component.css']
})

export class PostListComponent{
	
	public postlist : Post[];
	constructor(){
		this.postlist = new Array<Post>();
	}

	addPost(newLink:string) {
		var post = new Post(newLink);
		this.postlist.push(post);
	}
	upVote(post: Post){
		post.upVote();
	}

	downVote(post: Post){
		post.downVote();
	}

}