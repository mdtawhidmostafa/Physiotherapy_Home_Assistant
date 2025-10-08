function updateDistricts() {
  var divisionSelect = document.getElementById("division");
  var districtSelect = document.getElementById("district");
  var selectedDivision = divisionSelect.value;
  districtSelect.innerHTML = "";
  var option = document.createElement("option");
  option.value = "";
  option.text = "Select District";
  districtSelect.appendChild(option);
  if (selectedDivision === "dhaka") {
      var dhakaDistricts = ["Dhaka", "Faridpur", "Gazipur", "Gopalganj", "Kishoreganj", "Madaripur", "Manikganj", "Munshiganj", "Narayanganj", "Narsingdi", "Rajbari", "Shariatpur", "Tangail"];
      addOptions(districtSelect, dhakaDistricts);
  } else if (selectedDivision === "rajshahi") {
      var rajshahiDistricts = ["Rajshahi", "Bogra", "Joypurhat", "Naogaon", "Natore", "Chapainawabganj", "Pabna", "Sirajganj"];
      addOptions(districtSelect, rajshahiDistricts); 
  } else if (selectedDivision === "chittagong") {
      var chittagongDistricts = ["Chittagong", "Bandarban", "Brahmanbaria", "Chandpur", "Comilla", "Cox'sBazar", "Feni", "Khagrachhari", "Lakshmipur", "Noakhali", "Rangamati"];
      addOptions(districtSelect, chittagongDistricts);
  } else if (selectedDivision === "barisal") {
      var barisalDistricts = ["Barisal", "Barguna", "Bhola", "Jhalokati", "Patuakhali", "Pirojpur"];
      addOptions(districtSelect, barisalDistricts);
  } else if (selectedDivision === "khulna") {
      var khulnaDistricts = ["Khulna", "Bagerhat", "Chuadanga", "Jessore", "Jhenaidah", "Magura", "Meherpur", "Narail", "Satkhira"];
      addOptions(districtSelect, khulnaDistricts);
  } else if (selectedDivision === "mymensingh") {
      var mymensinghDistricts = ["Mymensingh", "Jamalpur", "Netrokona", "Sherpur"];
      addOptions(districtSelect, mymensinghDistricts);
  } else if (selectedDivision === "rangpur") {
      var rangpurDistricts = ["Rangpur", "Dinajpur", "Gaibandha", "Kurigram", "Lalmonirhat", "Nilphamari", "Panchagarh", "Thakurgaon"];
      addOptions(districtSelect, rangpurDistricts);
  } else if (selectedDivision === "sylhet") {
      var sylhetDistricts = ["Sylhet", "Habiganj", "Maulvibazar", "Sunamganj"];
      addOptions(districtSelect, sylhetDistricts);
  }
}

function addOptions(selectElement, optionsArray) {
  optionsArray.forEach(function(option) {
      var optionElement = document.createElement("option");
      optionElement.textContent = option;
      optionElement.value = option;
      selectElement.appendChild(optionElement);
  });
}
