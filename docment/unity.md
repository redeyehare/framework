[toc]



## dntnetty
### 模块理解
DotNetty.Common是公共的类库项目，包装线程池，并行任务和常用帮助类的封装

DotNetty.Transport是DotNetty核心的实现例如：Bootstrapping程序引l导类，Channels管道类（socket每有一个连接客户端就会创建一个channne）等等

DotNetty.Buffers是对内存缓冲区管理的封装（主要在接收和发出是对socket
通讯内容进行缓存管理）

DotNetty.Codes是对编码器解码器的封装，包括一些基础基类的实现，我们在项目中自定义的协议，都要继承该项目的特定基类和实现（该类库在整个通讯环节是重中之重）

DotNetty.Handlers封装了常用的管道处理器，比如Tls编解码，超时机制，心跳检查，日志等。(企业级开发中必不可少的处理类)


- BIO（同步阻塞）：客户端在请求数据的过程中，保持一个连接，不能做其他事情。

- NIO（同步非阻塞）：客户端在请求数据的过程中，不用保持一个连接，不能做其他事情。（不用保持一个连接，而是用许多个小连接，也就是轮询）

NIO有3个实体：Buffer（缓冲区），Channel（通道），Selector（多路复用器）

Buffer是客户端存放服务端信息的一个容器，服务端如果把数据准备好了。就会通过ChannelBuffer里面传。Buffer有7个类型：ByteBuffer、CharBuffer、DoubleBuffer、FloatBuffer、IntBuffer、LongBuffer、ShortBuffer

Channel是客户端与服务端之间的双工连接通道。所以在请求的过程中，客户端与服务端中间的Channel就读/写读/写读/写在不停的执行"连接、询问、断开"的过程。直到数据准备好。再通过channel传回来。

Selector是服务端选择Channel的一个复用器：Seletor有两个核心任务：1监控数据是否准备好，2应答Channel。具体说来，多个Channel反复轮询时。Selector就看该Channel所需的数据是否准备好了；如果准备好了．则将数据通过channel返回给该客户端的Buffer，该客户端再进行后续其他操作；如果没准备好.则告诉Channel还需要继续轮询：多个Channel反复询问Selector，Selector为这些Channel—一解答。

- AIO（异步非阻塞）：客户端在请求数据的过程中，不用保持一个连接，可以做其他事情。（客户端做其他事情，数据来了等服务端来通知。）


洗衣机洗衣服（无论阻塞式I0还是非阻塞式10，都是同步I0模型）

同步阻塞：你把衣服丢到洗衣机洗，然后看着洗衣机洗完，洗好后再去晾衣服(你就干等，啥都不做，阻塞在那边)

同步非阻塞：你把衣服丢到洗衣机洗，然后会客厅做其他事情，定时去阳台看洗衣机是不是洗完了，洗好后再去晾衣服（等待期间你可以做其他事情）

异步非阻塞：你把衣服丢到洗衣机洗，然后会客厅做其他事情，洗衣机洗好后会自动去晾衣服
晾完成后放个音乐告诉你洗好衣服并晾好了。



ExampleHelper. SetConsoleLogger();






## netcord






