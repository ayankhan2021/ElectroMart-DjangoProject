document.getElementById("btn11").addEventListener('click',function(){
    document.getElementById("log").classList.remove("active")
    document.getElementById("sign").classList.add("active")
    document.getElementById("sign").classList.remove("nonactive")
})
document.getElementById("btn22").addEventListener('click',function(){
    document.getElementById("sign").classList.remove("active")
    document.getElementById("log").classList.add("active")
    document.getElementById("sign").classList.add("nonactive")

})