import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.scss']
})
export class TodosComponent implements OnInit {

  value: string;
  constructor() { }

  todos = [
    {
      id: 1,
      title: "Get done",
      done: false
    },
    {
      id: 2,
      title: "Hello",
      done: false
    }
  ]
  ngOnInit() {
  }

  deleteTodo(id){
    this.todos = this.todos.filter(el => el.id !== id);
  }

  addTodo(){
    if(!this.value){
      alert("GIVE TODO");
      return
    }
    let todo = {
      id: this.todos.length + 1,
      title: this.value,
      done: false 
    }
    this.todos.push(todo);
    this.value = '';
  }

  changeStatus(id){
    this.todos.map(el => el.id == id ? el.done = !el.done : el.done);
    console.log(this.todos)
  }
}
