export class Post {
	public title: string;
	public url: string;
	public score: number;
	public topic: number;
	public pk: number;
	constructor(newLink: string, newTitle: string, newTopic: number){
		this.url = newLink;
		this.topic = newTitle;
		this.title= newTopic;
	}
}