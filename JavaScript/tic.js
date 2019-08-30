const buttonClick2 = document.querySelector('#btn-click')
const allTd = document.querySelectorAll('td')



console.log(buttonClick2)
console.log(allTd)


//next clear each tds

function clearBoard()
{
    for (let i = 0; i < allTd.length; i++)
    {
        allTd[i].textContent = ''
    }

}

buttonClick2.addEventListener('click', clearBoard)


//click to button
function changeMarker()
{
    if(this.textContent === '')
    {
        this.textContent = 'X'
    }
    else if(this.textContent === 'X')
    {
        this.textContent = 'O'
    }
    else
    {
        this.textContent=''
    }

}


//use for loop to add event listeners to all td's

for (let i = 0; i < allTd.length; i++)
{
    allTd[i].addEventListener('clck', changeMarker)
}





//allTd.addEventListener('click', changeMarker())
//
//buttonClick2.addEventListener('click', function()
//{
//    buttonClick.textContent = 'Change'
//    buttonClick.style.color = 'green'
//})