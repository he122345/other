package web.WsServer;

import javax.websocket.*;
import javax.websocket.server.ServerEndpoint;

/**
 * @author he
 * @date 2021/9/24
 * @time 16:26
 * @message
 */

@ServerEndpoint("/echo")
public class WebSocket {

    /**
     * 连接建立成功调用的方法
     * @param session  可选的参数。session为与某个客户端的连接会话，需要通过它来给客户端发送数据
     */
    @OnOpen
    public void onOpen(Session session){
        //与某个客户端的连接会话，需要通过它来给客户端发送数据
        System.out.println("有新连接加入");
    }

    /**
     * 连接关闭调用的方法
     */
    @OnClose
    public void onClose(){
        System.out.println("有一连接关闭");
    }


    @OnMessage
    public void onMessage(String message, Session session) {
        System.out.println("来自客户端的消息:" + message);
        //群发消息

    }


    @OnError
    public void onError(Session session, Throwable error){
        System.out.println("发生错误");
        error.printStackTrace();
    }
}
