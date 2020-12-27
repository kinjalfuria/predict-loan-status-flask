function getGenderValue() {
  var uiGender = document.getElementsByName("uiGender");
  for(var i in uiGender) {
    if(uiGender[i].checked) {
        return uiGender[i].value;

    }
  }
  return -1; // Invalid Value
}

function getMarriedValue() {
  var uiMarried = document.getElementsByName("uiMarried");
  for(var i in uiMarried) {
    if(uiMarried[i].checked) {
        return uiMarried[i].value;
    }
  }
  return -1; // Invalid Value
}

function getDependentsValue() {
  var uiDependents = document.getElementsByName("uiDependents");
  for(var i in uiDependents) {
    if(uiDependents[i].checked) {
        return uiDependents[i].value;
    }
  }
  return -1; // Invalid Value
}

function getEducation() {
  var uiEdu = document.getElementsByName("uiEdu");
  for(var i in uiEdu) {
    if(uiEdu[i].checked) {
        return uiEdu[i].value;
    }
  }
  return -1; // Invalid Value
}

function getEmployed() {
  var uiEmp = document.getElementsByName("uiEmp");
  for(var i in uiEmp) {
    if(uiEmp[i].checked) {
        return uiEmp[i].value;
    }
  }
  return -1; // Invalid Value
}


function getPropertyArea() {
  var uiProperty = document.getElementsByName("uiProperty");
  for(var i in uiProperty) {
    if(uiProperty[i].checked) {
        return uiProperty[i].value;
    }
  }
  return -1; // Invalid Value
}

function getCreditHistory() {
  var uiCredit = document.getElementsByName("uiCredit");
  for(var i in uiCredit) {
    if(uiCredit[i].checked) {
        return uiCredit[i].value;
    }
  }
  return -1; // Invalid Value
}

function getLoanTerm() {
  var uiLat = document.getElementsByName("uiLat");
  for(var i in uiLat) {
    if(uiLat[i].checked) {
        return uiLat[i].value;
    }
  }
  return -1; // Invalid Value
}

function onClickedLoanStatus() {
  console.log("Loan Status button clicked");

  var loanamount = document.getElementById("uiloanamt");
  
  var applicantincome = document.getElementById("uiappinc");
  var coapplicantincome = document.getElementById("uicoappinc");

  var gender1 = getGenderValue();
  var married1 = getMarriedValue();
  var dependents1 = getDependentsValue();
  var emp1 = getEmployed();
  var edu1 = getEducation();
  var property1 = getPropertyArea();
  var credit1 = getCreditHistory();
  var loanterm1 = getLoanTerm()

  var loanStatus = document.getElementById("uiLoanStatus");



   var url = "/predict_status";


  $.post(url, {
      applicant_income: parseInt(applicantincome.value),
      co_income: parseFloat(coapplicantincome.value),
      loan_amount: parseFloat(loanamount.value),
      gender: gender1,
      married: married1,
      dependents: dependents1,
      edu: edu1,
      emp: emp1,
      loan_term: loanterm1,
      credit_hist: credit1,
      property_area: property1
      
  },function(data, status) {
      console.log(data.loan_status);
      var str="";
      if (parseInt(data.loan_status) == 1){
      str = "Approved";}
      else{
      str="Rejected";}
      loanStatus.innerHTML = "<h2>" + str + "</h2>";
      console.log(status);
  });
}

