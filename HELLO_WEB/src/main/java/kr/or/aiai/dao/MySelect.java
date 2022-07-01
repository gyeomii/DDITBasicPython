package kr.or.aiai.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class MySelect {
	public static void main(String[] args) {
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;

		try {
			
			//String driver = "org.mariadb.jdbc.Driver";
			String driver = "com.mysql.cj.jdbc.Driver";
			
			//String url = "jdbc:mariadb://localhost:3305/python";
			String url = "jdbc:mysql://localhost:3305/python";
			String user = "root";
			String pw = "python";
			
			Class.forName(driver);
			
			conn = DriverManager.getConnection(url, user, pw);
			
			stmt = conn.createStatement();
			
			String sql = "select * from emp";
			
			rs = stmt.executeQuery(sql);

			while (rs.next()) {
				String id = rs.getString("e_id");
				String name = rs.getString("e_name");
				String sex = rs.getString("sex");
				String addr = rs.getString("addr");

				System.out.println(id + " " + name + " " + sex + " " + addr);
			}
		} catch (SQLException | ClassNotFoundException e) {
			e.printStackTrace();
		} finally {
			try {rs.close();} catch (SQLException e) {e.printStackTrace();}
			try {stmt.close();} catch (SQLException e) {e.printStackTrace();}
			try {conn.close();} catch (SQLException e) {e.printStackTrace();}	
		}
	}
}
