
import {Component} from 'angular2/core';
import {PostListComponent} from './post_list.component';
import {HTTP_PROVIDERS}    from 'angular2/http';
import {PostService}       from './post.service';


@Component({
    selector: 'my-app',
    templateUrl: 'app/templates/app.component.html',
    styleUrls: ['app/css/app.component.css'],
    directives: [
    	PostListComponent
    ]
    providers: [
    	HTTP_PROVIDERS,
    	PostService
    ]
})
export class AppComponent implements OnInit{

    public url:string= "../../images/background2.png";

    changeBackground() {
        if(this.url == "../../images/background2.png"){
            this.url = "../../images/background2-2.jpg";
        }
        else{
            this.url = "../../images/background2.png";
        }
    }
    ngOnInit() { 
        setInterval(()=>{this.changeBackground();}, 2000); 
    }

}			