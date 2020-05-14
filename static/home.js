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
            $("#B-clause").addClass("fade-out")
            setTimeout(() => {
                $("#B-clause").removeClass("fade-out")
                $("#B-clause").addClass("fade-in")
                $("#B-clause").text(B_clause.value + ", ") 
                $("#C-clause").addClass("fade-out")
            }, 3000);
            setTimeout(() => {
                $("#C-clause").removeClass("fade-out")
                $("#C-clause").addClass("fade-in")
                $("#C-clause").text(C_clause.value + ".") 
            }, 6000);
            setTimeout(() => {
                $("#generate-btn").prop("disabled", false)
            }, 9000);

            
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
    if($("#A-clause").text() == ""){
        $("#A-clause").addClass("fade-in")
        get_clauses()
    }
    else{    
        $("#A-clause").removeClass("fade-in")
        $("#A-clause").addClass("fade-out")
        setTimeout(() => {
            $("#A-clause").removeClass("fade-out")
            $("#A-clause").addClass("fade-in")
            get_clauses()
        }, 3000);
    }

})