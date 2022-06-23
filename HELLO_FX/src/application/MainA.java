package application;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class MainA extends Application {
	Parent root;
	Scene scene;
	Button btn;
	TextField tf1;
	TextField tf2;
	TextField tf3;
	TextField tf4;

	@Override
	public void start(Stage primaryStage) {
		try {
			root = FXMLLoader.load(getClass().getResource("mainA.fxml"));
			scene = new Scene(root, 800, 150); // (width, height)
			btn = (Button) scene.lookup("#btn");
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			tf3 = (TextField) scene.lookup("#tf3");
			tf4 = (TextField) scene.lookup("#tf4");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				public void handle(Event event) {
					calc();
				}
			});
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void calc() {
		int n1 = Integer.parseInt(tf1.getText());
		int n2 = Integer.parseInt(tf2.getText());
		int n3 = Integer.parseInt(tf3.getText());
		int result = 0;
		for (int i = n1; i <= n2; i++) {
			if (i % n3 == 0) {
				result += i;
			}
		}
		String str = String.valueOf(result);
		tf4.setText(str);
	}

	public static void main(String[] args) {
		launch(args);
	}
}