/*

Your task is to design a simple EventEmitter class in JavaScript. This class should have the following methods:

    subscribe(eventName, callback) - This method should allow a listener to register a callback to be invoked whenever a specific event is fired.

    emit(eventName, data) - This method should trigger all the callbacks associated with the given eventName, passing the provided data to each of the callbacks.

    unsubscribe(eventName, callback) - This method should allow a listener to stop receiving notifications of a specific event.


    Pubsub pattern, in nodejs in node and distributed systems. mediated through brokers and queues. 

    instance of event emitter in two different parts of application. In one location we want to know what happens with a event. will emit data for foo

    In another part,subscribed to foo. 
    subscriber,will have its function invoked and pass foo it's data. 
    invoked and passed the data. 

    One instance of event emitter

    eventName: foo

    B -> subscribe (foo)
    A -> foo
    B <- foo (data)

           x           x
    [0, 1, 2, 3, 4, 5, 6]


*/

class EventEmitter {
    constructor() { 
      this.subscribers = {}
    }
  // creating a relationship between callback and event name
  //string is topic name, callback is 
  // each subscriber has the same event name, but different callback
  // have to invoke all callbacks associated with event name
    subscribe(eventName, callback) { 
      if (this.subscribers[eventName]){
      this.subscribers[eventName].push(callback)
      } else {
        this.subscribers[eventName] = [callback]
      }
  
      // bind event name to callback
        // ensure eventName is populated this.subscr..
        // if not do this
        // else do that
    }
    // the data from emitter passed to the callback 
    emit(eventName, data) { 
      //iterate over the callbacks in the subscribers object value at eventName
      if (this.subscribers[eventName]) {
        this.subscribers[eventName].forEach((cb) => (
          cb(data)
        ))
      }
    }
    // for a given event, we are deregistering callback for invocation 
    unsubscribe(eventName, callback) { 
      if (this.subscribers[eventName]){
       const index = this.subscribers[eventName].indexOf(callback);
       this.subscribers[eventName] = this.subscribers[eventName].filter(el => (
          el !== callback
       ));
      }
    }
  }
  
  const eventEmitter = new EventEmitter();
  
  const returnFoo = (string) => {
  
    console.log(string + 'Foo')
  }
  eventEmitter.subscribe('listenForPost', returnFoo)
  
  
  const returnBar = string => {
    console.log(string + 'Bar')
  }
  
  eventEmitter.subscribe('listenForPost', returnBar)
  
  eventEmitter.emit('listenForPost', "Hi, there")
  
  eventEmitter.unsubscribe('listenForPost', returnBar)
  
  
  eventEmitter.emit('listenForPost', "Hi, there")
  
  eventEmitter.unsubscribe('listenForPost', returnFoo)
  
  eventEmitter.emit('listenForPost', "Hi, there")
  
  
  
  /*
  
  1. Clarify requirements through questioning, but also (most importantly) concrete examples
  2. Write test cases. Creating the instance, utilizing it with different arguments. Identifying and covering possible edge cases.  
  3. Try to solve the problem conceptually in pseudo. (not a full implementation, but just to cover primary underlying logic)
  4. Proceed with a concrete implementation
  
  */