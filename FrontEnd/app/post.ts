export class Post {
	public link: string;
	private vote : number;
	constructor(newLink: string){
		this.link = newLink;
		this.vote = 0;
	}
	upVote(){
		this.vote++;
	}
	downVote(){
		if(this.vote){
			this.vote--;
		}
	}
}