


var intToRoman = function(num) {

    let hash = new Map();
    hash.set(1, "I");
    hash.set(4, "IV");
    hash.set(5, "V");
    hash.set(9, "IX");
    hash.set(10,"X");   
    hash.set(40, "XL");
    hash.set(50, "L");
    hash.set(90, "XC");
    hash.set(100,"C");
    hash.set(400, "CD");
    hash.set(500, "D");
    hash.set(900, "CM");
    hash.set(1000, "M");

    if (hash.has(num)) return hash.get(num);
    let result = '';
    let times, remainder; 
    
    while (num){
        if (num >= 1000){
            let times = Math.floor(num/1000);
            let remainder = num%1000;
            num = remainder;
            result += (hash.get(1000).repeat(times))
        }
        if (num >= 900){
            let times = Math.floor(num/900);
            let remainder = num%900;
            num = remainder;
            result += (hash.get(900).repeat(times))
        }
        if (num >= 500){
            let times = Math.floor(num/500);
            let remainder = num%500;
            num = remainder;
            result += (hash.get(500).repeat(times))
        }
        if (num >= 400){
            let times = Math.floor(num/400);
            let remainder = num%400;
            num = remainder;
            result += (hash.get(400).repeat(times))
        }
        if (num >= 100){
            let times = Math.floor(num/100);
            let remainder = num%100;
            num = remainder;
            result += (hash.get(100).repeat(times))
        }
        
        if (num >= 90){
            let times = Math.floor(num/90);
            let remainder = num%90;
            num = remainder;
            result += (hash.get(90).repeat(times))
        }
        if (num >= 50){
            let times = Math.floor(num/50);
            let remainder = num%50;
            num = remainder;
            result += (hash.get(50).repeat(times))
        }
        if (num >= 40){
            let times = Math.floor(num/40);
            let remainder = num%40;
            num = remainder;
            result += (hash.get(40).repeat(times))
        }
        if (num >= 10){
            let times = Math.floor(num/10);
            let remainder = num%10;
            num = remainder;
            result += (hash.get(10).repeat(times))
        }
        if (num >= 9){
            let times = Math.floor(num/9);
            let remainder = num%9;
            num = remainder;
            result += (hash.get(9).repeat(times))
        }
        if (num >= 5){
            let times = Math.floor(num/5);
            let remainder = num%5;
            num = remainder;
            result += (hash.get(5).repeat(times))
        }

        if (num >= 4){
            let times = Math.floor(num/4);
            let remainder = num%4;
            num = remainder;
            result += (hash.get(4).repeat(times))
        }
        if (num >= 1){
            let times = Math.floor(num/1);
            let remainder = num%1;
            num = remainder;
            result += (hash.get(1).repeat(times))
        }


    }
return result;  
    
};

console.log(intToRoman(58))