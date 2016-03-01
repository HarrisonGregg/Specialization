import {Injectable}     from 'angular2/core';
import {Http, Response} from 'angular2/http';
import {Post}           from './post';
import {Observable}     from 'rxjs/Observable';

@Injectable()
export class PostService {
  constructor (private http: Http) {}

  private _postlistUrl = 'http://education-project.heroku.com/topicLinks/Bananas/';  // URL to web api

  getPostList () {
  	console.log("services get called")
    return this.http.get(this._postlistUrl)
                    .map(res => <Post[]> res.json().data)
                    .catch(this.handleError);
  }
  private handleError (error: Response) {
    // in a real world app, we may send the error to some remote logging infrastructure
    // instead of just logging it to the console
    console.error(error);
    return Observable.throw(error.json().error || 'Server error');
  }
}