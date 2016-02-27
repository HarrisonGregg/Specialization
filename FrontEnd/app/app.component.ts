
import {Component} from 'angular2/core';
import {PostListComponent} from './post_list.component';

@Component({
    selector: 'my-app',
    templateUrl: 'app/templates/app.component.html',
    directives: [
    	PostListComponent
    ]
})
export class AppComponent {

}			