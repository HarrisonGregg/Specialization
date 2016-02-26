import {Component} from 'angular2/core';
import {Post} from './post';

@Component({
	selector: 'post-list',
	template: `
		<input #newLink
      		(keyup.enter)="addPost(newLink.value)"
      		(blur)="newLink.value='' ">

    	<button (click)=addPost(newLink.value)>PostLink</button>
    	<ul>
    		<li *ngFor="#post of postlist">{{post.link}}
    			<button (click)=upVote(post)>upvote</button>
    			<button (click)=downVote(post)>downvote</button>
    			<div>vote = {{ post.vote }}</div>
    		</li>
    	</ul>
	`
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