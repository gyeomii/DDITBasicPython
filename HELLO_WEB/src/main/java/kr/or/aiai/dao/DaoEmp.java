package kr.or.aiai.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class DaoEmp {

	public ArrayList<EmpVO> getList() throws Exception {
		ArrayList<EmpVO> list = new ArrayList<EmpVO>();
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;

		// String driver = "org.mariadb.jdbc.Driver";
		String driver = "com.mysql.cj.jdbc.Driver";

		// String url = "jdbc:mariadb://localhost:3305/python";
		String url = "jdbc:mysql://localhost:3305/python";
		String user = "root";
		String pw = "python";

		Class.forName(driver);

		conn = DriverManager.getConnection(url, user, pw);

		stmt = conn.createStatement();

		String sql = "select * from emp";

		rs = stmt.executeQuery(sql);

		while (rs.next()) {
			String e_id = rs.getString("e_id");
			String e_name = rs.getString("e_name");
			String sex = rs.getString("sex");
			String addr = rs.getString("addr");

			EmpVO temp = new EmpVO();
			temp.setE_id(e_id);
			temp.setE_name(e_name);
			temp.setSex(sex);
			temp.setAddr(addr);

			list.add(temp);
		}

		rs.close();

		stmt.close();

		conn.close();

		return list;
	}

	public int insertEmp(EmpVO vo) throws Exception {

		Connection conn = null;
		PreparedStatement pstmt = null;

		// String driver = "org.mariadb.jdbc.Driver";
		String driver = "com.mysql.cj.jdbc.Driver";

		// String url = "jdbc:mariadb://localhost:3305/python";
		String url = "jdbc:mysql://localhost:3305/python";
		String user = "root";
		String pw = "python";

		Class.forName(driver);

		conn = DriverManager.getConnection(url, user, pw);

		String sql = "Insert into emp values(?,?,?,?)";

		pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, vo.getE_id());
		pstmt.setString(2, vo.getE_name());
		pstmt.setString(3, vo.getSex());
		pstmt.setString(4, vo.getAddr());

		int cnt = pstmt.executeUpdate();

		pstmt.close();
		conn.close();

		return cnt;
	}
}
