package kr.or.aiai.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class MyUpdate {
	public static void main(String[] args) {
		Connection conn = null;
		PreparedStatement pstmt = null;

		try {
			
			//String driver = "org.mariadb.jdbc.Driver";
			String driver = "com.mysql.cj.jdbc.Driver";
			
			//String url = "jdbc:mariadb://localhost:3305/python";
			String url = "jdbc:mysql://localhost:3305/python";
			String user = "root";
			String pw = "python";
			
			Class.forName(driver);
			
			conn = DriverManager.getConnection(url, user, pw);
			
			String sql = "Update emp set e_name=?, sex=?, addr=? where e_id=?";
			
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, "4");
			pstmt.setString(2, "4");
			pstmt.setString(3, "4");
			pstmt.setInt(4, 3);
			
			int cnt = pstmt.executeUpdate();
			if(cnt > 0) {
				System.out.println(cnt + "개의 데이터가 수정되었습니다");				
			}else {
				System.out.println("데이터 추가 실패");
			}

			
		} catch (SQLException | ClassNotFoundException e) {
			e.printStackTrace();
		} finally {
			try {pstmt.close();} catch (SQLException e) {e.printStackTrace();}
			try {conn.close();} catch (SQLException e) {e.printStackTrace();}	
		}
	}
}
