<%@page import="kr.or.aiai.dao.EmpVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet"
	href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script
	src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<!-- <script src="../js/jquery-3.6.0.min.js"></script> -->
<script
	src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<title>Insert title here</title>
</head>
<body>
	<%
	EmpVO pvo = (EmpVO) request.getAttribute("pvo");
	%>
	<form action="emp_mod" class="form-inline col-md-6">
		<div class="form-group col-md-6">
			<table class="table table-borderedcol-md-6">
				<tr>
					<th>사번</th>
					<td><input type="text" class="form-control" name="e_id" value="<%=pvo.getE_id()%>"/></td>
				</tr>
				<tr>
					<th>이름</th>
					<td><input type="text" class="form-control" name="e_name" value="<%=pvo.getE_name()%>"/></td>
				</tr>
				<tr>
					<th>성별</th>
					<td><input type="text" class="form-control" name="sex" value="<%=pvo.getSex()%>"/></td>
				</tr>
				<tr>
					<th>주소</th>
					<td><input type="text" class="form-control" name="addr" value="<%=pvo.getAddr()%>"/></td>
				</tr>
			</table>
			<input type="submit" class="btn btn-primary" value="실행">
			<p><%=msg%></p>
			<input type="button" class="btn btn-default" value="메인으로 돌아가기"
				onclick="location.href='emp_list'">
		</div>
	</form>

</body>
</html>