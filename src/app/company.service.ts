import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Company, Vacancy } from './app.component';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  private BASE_URL = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  getAllCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(
      `${this.BASE_URL}/companies/`
      );
  }

  getVacanciesByCompany(companyId: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(
      `${this.BASE_URL}/companies/${companyId}/vacancies/`
      );
  }

}
