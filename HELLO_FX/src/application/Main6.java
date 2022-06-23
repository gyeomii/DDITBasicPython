package application;

import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.stage.Stage;

public class Main6 extends Application {
	Parent root;
	Scene scene;
	Button btn;
	Label lbl1;
	Label lbl2;
	Label lbl3;
	Label lbl4;
	Label lbl5;
	Label lbl6;

	@Override
	public void start(Stage primaryStage) {
		try {
			root = FXMLLoader.load(getClass().getResource("main6.fxml"));
			scene = new Scene(root, 250, 250); // (width, height)
			btn = (Button) scene.lookup("#btn");
			lbl1 = (Label) scene.lookup("#lbl1");
			lbl2 = (Label) scene.lookup("#lbl2");
			lbl3 = (Label) scene.lookup("#lbl3");
			lbl4 = (Label) scene.lookup("#lbl4");
			lbl5 = (Label) scene.lookup("#lbl5");
			lbl6 = (Label) scene.lookup("#lbl6");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					getLotto();
				}
			});
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void getLotto() {
		Random random = new Random();

		int[] lottoNum = new int[6];
		int temp;

		for (int i = 0; i < lottoNum.length; i++) {
			lottoNum[i] = random.nextInt(45) + 1;
			for (int j = 0; j < i; j++) { // 중복제거
				if (lottoNum[i] == lottoNum[j]) {
					i--;
					break;
				}
			}
		}
		for (int i = 0; i < lottoNum.length; i++) { // 내림차순 정렬
			for (int j = 0; j < i; j++) {
				if (lottoNum[i] < lottoNum[j]) {
					temp = lottoNum[i];
					lottoNum[i] = lottoNum[j];
					lottoNum[j] = temp;
				}
			}
		}
			lbl1.setText(String.valueOf(lottoNum[0]));
			lbl2.setText(String.valueOf(lottoNum[1]));
			lbl3.setText(String.valueOf(lottoNum[2]));
			lbl4.setText(String.valueOf(lottoNum[3]));
			lbl5.setText(String.valueOf(lottoNum[4]));
			lbl6.setText(String.valueOf(lottoNum[5]));
	}

	public static void main(String[] args) {
		launch(args);
	}
}