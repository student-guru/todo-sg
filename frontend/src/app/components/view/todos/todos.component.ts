import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.scss']
})
export class TodosComponent implements OnInit {

  constructor() { }

  todos = [
    "hi"
  ]
  ngOnInit() {
    // setTimeout(function() => {this.todos.push()},3000)
    setTimeout(() => {
      this.todos.push("markos")
    }, 300);
  }

}
