import {Component, OnInit} from 'angular2/core';
import {Post} from './post';
import {PostService} from './post.service'

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

export class PostListComponent implements OnInit{
	
	public postlist : Post[];

	constructor (private _postService: PostService) {
		this.postlist = new Array<Post>();
	}

  	errorMessage: string;

  	ngOnInit() { this.getPostList(); }
  	getPostList() {
  		console.log('component getpostlist called');
    	this._postService.getPostList()
                     	 .subscribe(
                          postlist => this.postlist = postlist,
                          error =>  this.errorMessage = <any>error);

  	}


	addPost(newLink:string) {
		var post = new Post(newLink);
		this.postlist.push(post);
		console.log(post.link);
	}

	upVote(post: Post){
		post.upVote();
	}

	downVote(post: Post){
		post.downVote();
	}

}