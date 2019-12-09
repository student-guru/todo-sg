import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})

export class TodoService {

  // Declarations
  readonly backend = 'http://localhost:8080/api/';


  constructor(private _http: HttpClient) { }


  GETtodos() {
    return this._http.get(this.backend + 'todo/all');
  }

  POSTtodo(title: string) {
    let params = new HttpParams().set('title', title);
    return this._http.post( this.backend + 'todo/', {}, {params: params});
  }

  PATCHtodo(id: any) {
    return this._http.patch( this.backend + 'todo/' + id,{});
  }

  DELETEtodo(id: any) {
    return this._http.delete( this.backend + "todo/" + id );
  }

}
