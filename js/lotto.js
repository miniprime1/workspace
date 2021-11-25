var lotto = [Math.floor(Math.random()*45), 
    Math.floor(Math.random()*45), 
    Math.floor(Math.random()*45), 
    Math.floor(Math.random()*45), 
    Math.floor(Math.random()*45), 
    Math.floor(Math.random()*45)
]

lotto.sort(function(a, b) {return a-b})
console.log(lotto)
