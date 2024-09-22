    let now = new Date();

    month = '' + (now.getMonth() + 1),
    day = '' + now.getDate(),
    year = now.getFullYear();

    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;

    let today = [year, month, day].join('-');
   
    document.getElementById("Today").innerHTML = today;
    
    let due = document.querySelectorAll("span#dueDate")

    let tasks = document.querySelectorAll("li")
    
    let i = 0
    while(i < tasks.length){
        tasks[i].addEventListener('click', (e)=> {
            if (getComputedStyle(e.target).textDecorationLine == "none"){
                e.target.style.textDecoration = 'line-through'
                
            }
           else{
                e.target.style.textDecoration = 'none'
            }
        })
        let early = Math.round((Date.parse(due[i].innerHTML)-Date.parse(today))/(1000 * 60 * 60 *24))
        let late = Math.round((Date.parse(today)-Date.parse(due[i].innerHTML))/(1000 * 60 * 60 *24)) 
        if(due[i].innerHTML > today){
            
            if(early === 1){
                due[i].innerHTML =`Due Tommorow`
                due[i].style.color = "red"
            }
            else{
                due[i].innerHTML =`Due  in ` + early + ' days'
            }
            
        }

        if(due[i].innerHTML == today){
            
            if(early === 0){
                due[i].innerHTML =`Due Today`
            }
            
            due[i].style.color = "red"
        }
        
        if(due[i].innerHTML < today){
            if(late === 1){
                due[i].innerHTML =`Due yesterday`
            }
            else{
                due[i].innerHTML =`Due ` + late + ' days ago'
            }
            due[i].style.color = "red"
        }
        i++
        
    }
    

    