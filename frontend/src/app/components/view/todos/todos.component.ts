import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Todo } from '../../../todo';
import { TodoService } from 'src/app/services/todo.service';


@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.scss']
})
export class TodosComponent implements OnInit {

  readonly backend = 'http://localhost:8080/api/';

  value: string;
  todos: any;

  constructor(private _todos: TodoService) { }

  
  ngOnInit() {
    this.getTodos();
  }


  // call GET from service
  getTodos(){
    this._todos.GETtodos().subscribe(todos => {
      this.todos = todos;
      if(this.todos)
        this.todos.sort((a,b) => a.id - b.id);
    })
  }

  // call POST from service 
  addTodo(){
    if(!this.value){
      alert("GIVE TODO");
      return
    }

    this._todos.POSTtodo(this.value).subscribe( res => {
      this.getTodos();
    })

    this.value = '';
  }

  // call DELETE from service
  deleteTodo(id){
    this._todos.DELETEtodo(id).subscribe(res => {
      this.getTodos();
    })
  }

  // call PATCH from service
  changeStatus(id){
    this._todos.PATCHtodo(id).subscribe(res => {
      this.getTodos();
    });
    
  }
}
