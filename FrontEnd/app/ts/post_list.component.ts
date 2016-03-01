import {Component, OnInit} from 'angular2/core';
import {Post} from './post';
import {PostService} from './post.service'

@Component({
	selector: 'post-list',
	templateUrl: 'app/templates/post_list.component.html',
	styleUrls: ['/app/css/post_list.component.html']
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