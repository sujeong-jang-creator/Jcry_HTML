import { Component, OnInit, Input } from '@angular/core';
import { Hero } from '../hero';

@Component({
  selector: 'app-hero-detail',
  templateUrl: './hero-detail.component.html',
  styleUrls: ['./hero-detail.component.scss']
})
export class HeroDetailComponent implements OnInit {

  // 부모한테서 hero를 받아오겠다.
  @Input() hero?: Hero;

  constructor() { }

  ngOnInit(): void {
  }
}
