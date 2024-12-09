import { Component, OnInit } from '@angular/core';
import { WebsocketService } from '../service/websocket.service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  message: string = '';
  receivedMessages: any[] = [];

  constructor(private websocketService: WebsocketService) {}

  ngOnInit(): void {
    this.websocketService.connect();
    this.websocketService.getMessages().subscribe(msg => {
      this.receivedMessages.push(msg);  
    });
  }

  sendMessage(event: any): void {
    event.preventDefault();
    this.websocketService.sendMessage(this.message);
    this.message = '';
  }
}
