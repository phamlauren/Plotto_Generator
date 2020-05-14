var get_clauses = function(){
       
    $.ajax({
        type: "POST",
        url: "random",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        success: function(result){
            var A_clause = result["A_clause"]
            var B_clause = result["B_clause"]
            var C_clause = result["C_clause"]


            $("#A-clause").text(A_clause.value + ", ")
            $("#A-clause").removeClass("hide-item")
            setTimeout(() => { 
                $("#B-clause").text(B_clause.value + ", ") 
                $("#B-clause").removeClass("hide-item")
            }, 2500);
            setTimeout(() => {
                $("#C-clause").text(C_clause.value + ".") 
                $("#C-clause").removeClass("hide-item")
            }, 5000);
            setTimeout(() => {
                $("#generate-btn").prop("disabled", false)
            }, 7500);

            
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).on("click", "#generate-btn", function(){
    $("#generate-btn").prop("disabled", true)
    $("#A-clause").text()
    $("#A-clause").addClass("hide-item")
    $("#B-clause").text()
    $("#B-clause").addClass("hide-item")
    $("#C-clause").text()
    $("#C-clause").addClass("hide-item")
    get_clauses()

})