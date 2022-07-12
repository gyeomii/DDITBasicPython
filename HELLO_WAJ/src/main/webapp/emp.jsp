<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="jquery-3.6.0.min.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<title>Insert title here</title>
<script>
function fn_list() {
	var param = "";
	param += "dummy=" + Math.random();
	param += "&a=777";
	$.ajax({
		url : "ajaxlist",
		data : param,
		dataType : "json",
		type : "post",
		async: false,
		success : function(res) {
			var list = res;
			var html = ``;
			for(var i=0;i<list.length;i++){
				var e_id = list[i].e_id;
				var e_name = list[i].e_name;
				var sex = list[i].sex;
				var addr = list[i].addr;
				html += `
				<tr>
					<td>`+ e_id +`</td>
					<td>`+ e_name +`</td>
					<td>`+ sex +`</td>
					<td>`+ addr +`</td>
				</tr>
				`;
			}
			$("#mylist").html(html);
		}
	});
}
</script>
</head>
<body onload="fn_list()">
<div class="container">
<table class="table table-bordered">
	<thead>
		<tr>
			<td>사번</td>
			<td>이름</td>
			<td>성별</td>
			<td>주소</td>
		</tr>
	</thead>
	<tbody id="mylist">
		<tr>
			<td>__</td>
			<td>__</td>
			<td>__</td>
			<td>__</td>
		</tr>
	</tbody>
</table>
</div>
<div class="container">
<table class="table table-bordered">
	<tr>
		<td>사번</td>
		<td>
			<input type="text" id="e_id" class="form-control" />
		</td>
	</tr>
	<tr>
		<td>이름</td>
		<td>
			<input type="text" id="e_name" class="form-control"/>
		</td>
	</tr>
	<tr>
		<td>성별</td>
		<td>
			<input type="text" id="sex" class="form-control"/>
		</td>
	</tr>
	<tr>
		<td>주소</td>
		<td>
			<input type="text" id="addr" class="form-control"/>
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<input type="button" value="추가" class="btn btn-primary"/>
			<input type="button" value="수정" class="btn btn-warning"/>
			<input type="button" value="삭제" class="btn btn-danger"/>
		</td>
	</tr>
</table>
</div>
</body>
</html>