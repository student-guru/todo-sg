import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  email : string;
  password : string;
  constructor(private router: Router) { }

  ngOnInit() {
  }
  
  login(){
    if(!(this.email && this.password)){
      alert('wrong credentials')
      this.email = '';
      this.password = '';
      return
    }
    else if(this.email === 'markos@markos.markos' && this.password === 'markos')
      this.router.navigate(['todos'])
    else{
      alert('no credentials')
      this.email = '';
      this.password = '';
      return
    }
  }
}
