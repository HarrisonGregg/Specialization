export class Post {
	public name: string;
	private pk : number;
	constructor(newLink: string){
		this.link = newLink;
		this.vote = 0;
	}
	upVote(){
		//this.vote++;
	}
	downVote(){
		//if(this.vote){
		//	this.vote--;
		//}
	}
}