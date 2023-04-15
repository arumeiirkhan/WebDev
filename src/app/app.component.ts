import { Component, OnInit } from '@angular/core';
import { CompanyService } from './company.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  constructor(
    private compService: CompanyService
  ){}
  title = 'hhFront';

  companies: Company[] = [];
  vacancies: Vacancy[] = [];
  selectedCompanyID?: number;
  vacanciesVisible = false;

  companySelected(company: Company) {
    if(company.id == this.selectedCompanyID){
      this.vacanciesVisible = false;
    } else{
      this.selectedCompanyID = company.id;
      this.compService.getVacanciesByCompany(this.selectedCompanyID).subscribe(vacancies => {
        this.vacancies = vacancies;
      });
      this.vacanciesVisible = true;
      }
  }

  ngOnInit(){
    this.compService.getAllCompanies().subscribe(companies => {
      this.companies = companies;
    });
  }
}

export interface Company{
  id:number,
  name:string;
  description:string;
  city:string;
  address:string;
}
export interface Vacancy{
  id:number,
  name: string;
  description: string;
  salary: number;
  company: Company;
}
