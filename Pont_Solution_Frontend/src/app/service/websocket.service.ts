import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { webSocket } from 'rxjs/webSocket';

@Injectable({
  providedIn: 'root'
})
export class WebsocketService {
  private socket: any;
  private subject: Subject<any>;

  constructor() {
    this.subject = new Subject();
  }

  connect(): void {
    this.socket = webSocket('ws://localhost:8000/ws/chat_pont_solution/');

    this.socket.subscribe(
      (msg: any) => this.subject.next(msg),
      (err: any) => console.error(err),
      () => console.log('Connection closed')
    );
  }

  sendMessage(message: string): void {
    this.socket.next({ message: message });
  }

  getMessages(): Observable<any> {
    return this.subject.asObservable();
  }
}
