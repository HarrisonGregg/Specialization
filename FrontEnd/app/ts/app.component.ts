
import {Component} from 'angular2/core';
import {PostListComponent} from './post_list.component';
import {HTTP_PROVIDERS}    from 'angular2/http';
import {PostService}       from './post.service';


@Component({
    selector: 'my-app',
    templateUrl: 'app/templates/app.component.html',
    directives: [
    	PostListComponent
    ]
    providers: [
    	HTTP_PROVIDERS,
    	PostService
    ]
})
export class AppComponent {

}			