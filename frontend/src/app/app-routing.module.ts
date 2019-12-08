import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/view/home/home.component';
import { TodosComponent } from './components/view/todos/todos.component';


const routes: Routes = [
  {path: "", component: HomeComponent},
  {path: "todos", component: TodosComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
