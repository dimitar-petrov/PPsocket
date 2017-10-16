<?php

class SocketHelper{
   
   public $socket;

   public function __construct($unix_socket){
       $this->socket = socket_create(AF_UNIX, SOCK_DGRAM, 0);
   	   $result = socket_connect($this->socket, $unix_socket);
   }

   public function send_data($content){
       socket_write($this->socket, 100000 + strlen($content), 6);
       socket_write($this->socket, $content, strlen($content));
   }

   public function close_socket(){
   	   socket_close($this->socket);
   }
}
