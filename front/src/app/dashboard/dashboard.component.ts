import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {first} from 'rxjs/operators';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';

import {User} from '../models';
import {Article} from '../models';
import {AlertService, ArticleService, AuthenticationService} from '../services';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit, OnDestroy {
  searchForm: FormGroup;
  currentUser: User;
  currentUserSubscription: Subscription;
  articles: Article[] = [];
  submitted = false;
  loading = false;


  constructor(private formBuilder: FormBuilder,
              private authenticationService: AuthenticationService,
              private articleService: ArticleService,
              private alertService: AlertService
  ) {
    this.currentUserSubscription = this.authenticationService.currentUser
      .subscribe(user => {
        this.currentUser = user;
      });
  }

  ngOnInit() {
    this.searchForm = this.formBuilder.group({
      keyword: ['', [Validators.required,
        Validators.minLength(2),
        Validators.maxLength(128)]],
      type: ['Index', Validators.required],
    });
    this.loadAllArticles();
  }

  // convenience getter for easy access to form fields
  get f() {
    return this.searchForm.controls;
  }

  onSubmit() {
    this.submitted = true;

    // stop here if form is invalid
    if (this.searchForm.invalid) {
      return;
    }

    this.loading = true;
    this.articleService.findArticleByKeyword(this.searchForm.value)
      .pipe(first())
      .subscribe(
        data => {
          this.loading = false;
          if (data) {
            this.alertService.success("Articles have been found " + data.length, true)
          }
        },
        error => {
          this.alertService.error(error);
          this.loading = false;
        });
  }

  ngOnDestroy() {
    // unsubscribe to ensure no memory leaks
    this.currentUserSubscription.unsubscribe();
  }

  private loadAllArticles() {
    this.articleService.getAll().pipe(first()).subscribe(articles => {
      this.articles = articles;
    });
  }

}
