import { Routes, RouterModule } from '@angular/router';
import {AuthGuard} from "./helpers";
import {DashboardComponent} from "./dashboard/dashboard.component";
import {AuthComponent} from "./auth";
import {RegComponent} from "./reg";


const routes: Routes = [
    { path: '', component: DashboardComponent, canActivate: [AuthGuard] },
    { path: 'login', component: AuthComponent },
    { path: 'register', component: RegComponent },

    // otherwise redirect to home
    { path: '**', redirectTo: '' }
];

export const AppRoutingModule = RouterModule.forRoot(routes);
