import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Todo } from '../../../todo';


@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.scss']
})
export class TodosComponent implements OnInit {

  readonly backend = 'http://localhost:3000/';

  value: string;
  todos: any;

  constructor(private http: HttpClient) { }

  
  ngOnInit() {
    this.getTodos();
  }

  getTodos(){
    this.todos = this.http.get(this.backend + 'todos')
  }

  deleteTodo(id){
    let params = new HttpParams().set('id', id);
    this.http.delete(this.backend + 'todos',{ params })
    this.getTodos();
  }

  addTodo(){
    if(!this.value){
      alert("GIVE TODO");
      return
    }

    let todo = {
      title: this.value
    }
    this.http.post( this.backend + '/todos', todo).subscribe(
      res => console.log(res)
    )
  }

  changeStatus(id){
    let params = new HttpParams().set('id', id);
    this.http.put(this.backend + '/todos', { params });
  }
}
