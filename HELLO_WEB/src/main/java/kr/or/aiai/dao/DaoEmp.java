package kr.or.aiai.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class DaoEmp {

	public EmpVO getOne(String e_id) throws Exception {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;

		// String driver = "org.mariadb.jdbc.Driver";
		String driver = "com.mysql.cj.jdbc.Driver";

		// String url = "jdbc:mariadb://localhost:3305/python";
		String url = "jdbc:mysql://localhost:3305/python";
		String user = "root";
		String pw = "python";

		Class.forName(driver);

		conn = DriverManager.getConnection(url, user, pw);

		String sql = "select e_id, e_name, sex, addr from emp where e_id=?";

		pstmt = conn.prepareStatement(sql);

		pstmt.setString(1, e_id);
		
		rs = pstmt.executeQuery();

		EmpVO temp = new EmpVO();
		while (rs.next()) {
			e_id = rs.getString("e_id");
			String e_name = rs.getString("e_name");
			String sex = rs.getString("sex");
			String addr = rs.getString("addr");

			temp.setE_id(e_id);
			temp.setE_name(e_name);
			temp.setSex(sex);
			temp.setAddr(addr);

		}

		rs.close();
		pstmt.close();
		conn.close();

		return temp;
	}
	
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

		String sql = "select e_id, e_name, sex, addr from emp";

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

	public int updateEmp(EmpVO vo) throws Exception {
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

		String sql = "Update emp set e_name=?, sex=?, addr=? where e_id=?";

		pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, vo.getE_name());
		pstmt.setString(2, vo.getSex());
		pstmt.setString(3, vo.getAddr());
		pstmt.setString(4, vo.getE_id());

		int cnt = pstmt.executeUpdate();

		pstmt.close();
		conn.close();
		return cnt;
	}

	public int deleteEmp(String e_id) throws Exception {
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

		String sql = "Delete from emp where e_id=?";

		pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, e_id);

		int cnt = pstmt.executeUpdate();

		pstmt.close();
		conn.close();

		return cnt;

	}
}
