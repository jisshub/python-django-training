//objects in js

var car =
{
    name: 'baleno',
    company: 'maruti',
    price: '500000',
    airbags: true,
    getInsurance: function func1()
    {
        return true
    },
    changePrice: function func2(price)
    {
        this.price = price
        return price
    }
    ,
    changeName: function func3()
    {
       this.name = name
       return name
    }
}

//console.log(car)
//console.log(car.airbags)
//console.log(car.company)
console.log(car.getInsurance())
console.log(car.changePrice(90000))
console.log(car.changeName('Santro'))

//iterating thru each value of key
for (const value in car)
{
    console.log(car[value])

}





