package day24;

import java.awt.Frame;
import java.awt.Graphics;

public class FramePaint extends Frame{
	int cnt = 0;
	@Override
	public void paint(Graphics g) {
		g.drawLine(0, 0, 200, 200);
		g.drawString("hoho"+cnt, 100, 100);
		cnt++;
		super.paint(g);
	}
	public static void main(String[] args) {
		//생성
		FramePaint fp = new FramePaint();
		//사이즈
		fp.setSize(400, 400);
		//비지블
		fp.setVisible(true);
	}
}
