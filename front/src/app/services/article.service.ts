import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

import {Article, SearchRequest} from '../models';

@Injectable({providedIn: 'root'})
export class ArticleService {
  constructor(private http: HttpClient) {
  }

  getAll(limit=5, offset=1) {
    return this.http.get<Article[]>(`/articles?limit=`
      + limit
      + `&offset=`
      + offset);
  }

  findArticleByKeyword(searchReq: SearchRequest) {
    return this.http.post<Article[]>('/articles', searchReq)
  }
}
