let array=[];

function cat(name){
    this.name = name;
}

function func() {
    this.name = item_1.value;
    mycat = new cat(this.name)
    array.push(mycat)

    document.getElementById("myList").innerHTML = "";

    let list = document.getElementById("myList");

    array.forEach((item)=>{
        let li = document.createElement("li");
        li.innerText = item.name;
        list.appendChild(li);
    })
}

function del() {
    this.name = del_item.value;

    var i = 0;
    array.forEach((item)=>{
        console.log(item.name);
        if (item.name == del_item.value){
            array.splice(i, 1)
        }
        i++;
    })

    //array.push(mycat)
    document.getElementById("myList").innerHTML = "";
    let list = document.getElementById("myList");

    array.forEach((item)=>{
        let li = document.createElement("li");
        li.innerText = item.name;
        list.appendChild(li);
    })
}


//mycat = cat('Маруся', 12);
//print_str('Hello')