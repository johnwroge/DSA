



var evalRPN = function(tokens) {
    //create a stack data structure to store the tokens
    const stack = [];
    //iterate over the tokens array
    for (let i = 0; i < tokens.length; ++i){
        let token = tokens[i];
        //check if the type of the element is a number  
        if (!isNaN(token)){
     
            stack.push(Number(token));
        } else {
            console.log(stack)
            let first = stack.pop();
            //remove the last two elements from the stack
            let second = stack.pop();
            
            //el 1 and el2 and perform operation from left to right
            let value = operate(token,second, first)
            //push this element back onto stack
            stack.push(value)
        }
    }
       
    
    //return the element at position 0

return stack[0];
};


const operate = (operation, a, b) => {

         switch (operation){
        case "+":
          return a + b;
          break;
        case "-":
          return a - b;
          break;
        case "*":
          return a * b;
          break;
        case "/":
          return a / b >= 0 ? Math.floor(a / b) : Math.ceil(a / b)
          break;
        default:
          console.log("Invalid operator string");
   }
}


console.log(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))